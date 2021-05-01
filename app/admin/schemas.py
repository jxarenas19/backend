from app.ext import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("email", "phone", "name",
                  "company", "manager", "budget",
                  "message","from_pg","option_n","status")
