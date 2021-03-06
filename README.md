# Small Django Project with Rest APIs and GraphQL APIs

## Getting started
Install requirements

```
pip install -r requirements.txt
```
Create Database in Postgres (name:djangoapi)
```
python manage.py  migrate
```
Start server

```
python manage.py  runserver
```
Person and Car forms
```
http://127.0.0.1:8000/admin/personinfo/person/
http://127.0.0.1:8000/admin/personinfo/car/
```

Hit the RestAPIs

```
http://127.0.0.1:8000/api/person/
http://127.0.0.1:8000/api/car/
```

Hit the GraphQL APIs
```
http://127.0.0.1:8000/graphqlapi/
```

```
{
  persons{
    firstName
    lastName
    age
    cars{
      name
      year
    }
  }
  
  cars{
    name
    year
    person {
      firstName
    }
  }
  
  person(id:2){
    firstName
    lastName
  }
  
  car(id:1){
    name
    year
    person{
      firstName
    }
  }
}
```

```
mutation {
  createPerson(input:{firstName:"David", lastName:"Ahmadi", age:23, email:"David@gmail.com"}){
    ok
    person{
      firstName
      lastName
    }
  }
}


mutation {
  createCar(input:{name:"Renault Capture", year:2016, person:2}){
    ok
    car{
      name
      year
      person{
        firstName
        lastName
      }
    }
  }
}
```