<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.store_api_key(api_key="<value>", provider="openrouter")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from mix_python_sdk import Mix

async def main():

    async with Mix() as mix:

        res = await mix.authentication.store_api_key_async(api_key="<value>", provider="openrouter")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->