I. The project is for simple searching API. I focus on project structure / rate limit handling / containerizing

II. Run Project
Let run docker desktop and then run following commands:
- docker compose -f .\docker-compose.yml build
- docker compose -f .\docker-compose.yml up



III. API Docs
after running the app on local, let's access http://localhost:8000/docs

* example api curl for searching (import it to postman):
 curl --location 'http://0.0.0.0:8000/employees/search?location=remote' \
--header 'organization-id: organizationa' \
--data ''

* Be aware that project already has existed data each time it starts

IV. Special implements and TO DO
- I already implemented caching using redis for rate limit but because of limited time, I only layout the code, other than that I also using library slowapi for limmit request from a certain user within certain time
- I create db foder because in the future, may be project use different dbs


* TO DO
- I already created middleware for not only reate limit handling but also authen/author
- I also created exception_handler.py for handling exception and exception.py for custom exception
- For attribute "status" of employee, in code we should using enum to define values
- Pydantic is a power lib in fast, leverage it for validation request input
- Config folder for CORS, CSRF, JWT...
- Actually, I want to create DB with many tables (address, department, etc) but time dont allow me to do it
