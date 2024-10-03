from tortoise.models import Model
from tortoise import fields


class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        table = "tournament"
        default_connection = "default"


class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    tournament = fields.ForeignKeyField('models.Tournament',
                                        related_name='events')
    participants = fields.ManyToManyField('models.Team',
                                          related_name='events',
                                          through='event_team')

    def __str__(self):
        return self.name

    class Meta:
        table = "event"
        default_connection = "default"


class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        table = "team"
        default_connection = "default"
