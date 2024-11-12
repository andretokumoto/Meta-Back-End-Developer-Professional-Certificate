http_status = 400

match http_status:
    case 200:
        print('success')
    case 400:
        print('Bad request')
    case 404:
        print('Not found')