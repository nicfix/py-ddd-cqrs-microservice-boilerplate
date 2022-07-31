# Pydantic for Data Transfer Objects, Validation and Serialization

# Status

approved

# Context

Python is a dynamically typed language that has an extremely powerful data structure, the dictionary (a.k.a. `dict`).
Whereas the `dict` is a good choice for many scenarios I think that its usage was abused throughout the 
python projects I encountered in my career.

In many cases, data received from a http endpoint through parameters or POST body is represented
in the code as a dict. The same can be said for data returned from a Rest API that adopts the
JSON format as response. 

The simplicity of creating new dicts with literals often wins against the creation and the initialization
of a dedicated class.
  
This though brings, after some time, to problems related to the validation and the documentation
of what a `dict` instance contains throughout the code, problem that gets even worse when passing
the same dictionary throughout a deep stack of function calls.

# Solution

Use `pydantic` to represent data objects and validate your data.

Pydantic leverages on the combined power of:
* Python 3's type annotations
* `dataclasses` automatic constructors
* A validation framework based on reflection, that can be extended further using `@decorators`


# Consequences

For each endpoint that you define:
* Define an input data type using the `pydantic.BaseModel` class
* Define the output data type using the `pydantic.Basemodel` class


Example  
```python
import json
from typing import Optional
from pydantic import BaseModel

class MyEndpointInputDTO(BaseModel):
    my_resource_filter_id: str
    limit: Optional[int]=0
    offset: Optional[int]=0


class MyEndpointResourceDTO(BaseModel):
    id:str
    name:str
    age:int

def my_get_endpoint(params:dict) -> dict:
    
    input_data =MyEndpointInputDTO(**params)

    # ... do whatever ...

    my_resources = inner_function()

    return json.dumps([resource.dict() for resource in my_resources])
```

As you can see the code results really clean in the happy path.
Now if we want to handle the validation of the input parameters we just need to handle
and exception from `pydantic`.

```python

def my_get_endpoint(params:dict) -> dict:
    try:
        input_data=MyEndpointInputDTO(**params)
    except ValidationError as e:
        return BadRequestResponse(e.json())
    # ... do whatever ...

    my_resources= inner_function()

    return json.dumps([resource.json() for resource in my_resources])
```

And this will return something like:
```json
[
  {
    "loc": [
      "my_resource_filter_id"
    ],
    "msg": "field required",
    "type": "value_error.missing"
  },
  {
    "loc": [
      "limit"
    ],
    "msg": "invalid int format",
    "type": "value_error.int"
  }
]
```


 