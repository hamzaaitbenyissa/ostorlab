"""Mixin to enable distributed storage for a group of agent replicas or for a single agent that needs reliable storage.

A typical use-case is ensuring that a message value is processed only once in case multiple other agent are producing
duplicates or similar ones.

Typical usage:

```python
    status_agent = agent_persist_mixin.AgentPersistMixin(agent_settings)
    status_agent.set_add('crawler_agent_asset_dna', dna)
    is_new = not status_agent.set_is_member()
```
"""
import redis

from ostorlab.runtimes import definitions as runtime_definitions


class AgentPersistMixin:

    def __init__(self, agent_settings: runtime_definitions.AgentSettings) -> None:
        """Initializes the mixin from the agent settings.

        Args:
            agent_settings:
        """
        if agent_settings.redis_url is None:
            raise ValueError('agent settings is missing redis url')
        self._redis_client = redis.Redis.from_url(agent_settings.redis_url)

    def set_add(self, key, value) -> bool:
        """Helper function that takes care of reporting if the specified DNA has been tested in the past, or mark it
        as tested.
        The method can be used to sync multiple agents that may encounter the same test input but need to test it
        only once.
        Storage is shared between agents, ensure the keys used are unique.

        Args:
            key: Set key.
            value: List of values to add to set.

        Returns:
            True if it is a new member, False otherwise.
        """
        return bool(self._redis_client.sadd(key, value))

    def set_is_member(self, key, value) -> bool:
        """Indicates whether value is member of the set identified by key.

        Args:
            key: The set key.
            value: The value to check.

        Returns:
            True if it is a member, False otherwise.
        """
        return self._redis_client.sismember(key, value)
