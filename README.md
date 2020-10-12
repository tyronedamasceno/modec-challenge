# modec-challenge

Application to management of an FPSO equipment.

## Documentation && try it out!

You can find a postman collection for the API and do some tests [on this page](https://www.getpostman.com/collections/f31003e88f3a5ae772ca)

The API was deployed in a cloud service, the base URL is https://modec-api.herokuapp.com/ and the postman collection is already doing requests for it.

For example, you can do a POST request for https://modec-api.herokuapp.com/api/v1/vessels to create a new vessel!

PS: *Note that the first request may take a while because it is a free service, so it goes to sleep mode when is not being used.*

## How to execute API?

If you want to run it in you local machine, the recommendation is to user Docker and docker-compose (if you need to install it on Ubuntu, I suggest [this tutorial](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/))

You just need to clone or download this repository, navigate into folder, then run the following commands:

`$ docker-compose build`

`$ docker-compose up -d`

Now, you have an running API on your localhost on the port 8000.

You may want have a local superuser, so run the command below and follow instructions.

`$ docker-compose run --rm web python manage.py createsuperuser`

You can use the provided credentials to access the admin interface on `https://localhost:8000/admin/`.

Also, you can run unit automated tests running the following command

`$ docker-compose run --rm web python manage.py test`

## Contact

I hope you enjoy it.

**Feel free** to contact me any time on telegram [*@tyronedamasceno*](https://t.me/tyronedamasceno) or *tyronedamasceno@gmail.com*
