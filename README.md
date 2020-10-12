# modec-challenge

Application to management of an FPSO equipment.

## How to execute API?

The recommendation is to user Docker and docker-compose (if you need to install it on Ubuntu, I suggest [this tutorial](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/))

You just need to clone or download this repository, navigate into folder, then run the following commands:

`$ docker-compose build`

`$ docker-compose up -d`

Now, you have an running API on your localhost on the port 8000.

You may want have a local superuser, so run the command below and follow instructions.

`$ docker-compose run --rm web python manage.py createsuperuser`

You can use the provided credentials to access the admin interface on `https://localhost:8000/admin/`.

## Documentation && try it out!

You can find a postman collection for the API and do some tests [on this page](...)

Also, you can run unit automated tests running the following command

`$ docker-compose run --rm web python manage.py test`

## Contact

I hope you enjoy it.

**Feel free** to contact me any time on telegram [*@tyronedamasceno*](t.me/tyronedamasceno) or *tyronedamasceno@gmail.com*
