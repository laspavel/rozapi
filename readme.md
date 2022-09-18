# Простое API для работы с Rozetka API на Python.

Пример использования:
```
import rozapi

....
rapi=rozapi.RozetkaAPI('RozetkaLogin','RozetkaPassword')
orders=rapi.api_request(api_type='get',api_method='orders/search',params={'page':str(page),'sort':'id'})
....

`


