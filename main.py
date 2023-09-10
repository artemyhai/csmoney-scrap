from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()
# print(ua.random)


def collect_data():
    # response = requests.get(
    #     url='https://cs.money/1.0/market/sell-orders?limit=60&minPrice=10000&offset=0&type=2',
    #     headers={'user-agent': f'{ua.random}'}
    # )

    # with open('result.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    batch_size = 60
    result = []
    count = 0
    
    while True:
        for item in range(offset, offset + batch_size, 60):
            # url = item 
            # print(url)
            
            url = f'https://cs.money/1.0/market/sell-orders?limit=60&minPrice=2300&offset={item}&type=2'
            reverse = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )
            
            offset += batch_size
            
            data = reverse.json()
            
            items = data.get('items')
            
            for i in items:
                if i.get('pricing')['discount'] is not None and i.get('pricing')['discount'] < -10:
                    item_full_name = i.get('asset')
                    item_price = i.get('pricing')
                    item_discount = i.get('pricing')
                    item_3d = i.get('links')
                    
                    result.append(
                        {
                           'full_name': item_full_name['names']['full'],
                           'price': item_price['default'],
                           'discount': item_discount['discount'],
                           '3d': item_3d['3d']
                        }
                    )
        
        count += 1
        print(f'Page #{count}')
        print(url)
                     
        if len(items) < 60:
            break
        
    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False) 
    
    print(len(result))


def main():
    collect_data()


if __name__ == '__main__':
    main()

# hello



