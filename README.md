# tortoise-demo
Very small demo for using tortoise-orm

The getting started page doesn't clearly define how to setup / structure your project to use tortoise-orm which will yield an error similar to the following:

```
tortoise.exceptions.ConfigurationError: default_connection for the model <class 'tortoise_demo.models.Tournament'> cannot be None
```

In order to resolve this, you need to define an inner class Meta in each model and define the table and default_connection options.

```
class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name

    # This...
    class Meta:
        table = "team"
        default_connection = "default" 

```

## Install

To try the demo, simply pull and run poetry install. Tested on 3.12.6