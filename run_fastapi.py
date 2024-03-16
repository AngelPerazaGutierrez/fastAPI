import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:my_backend', host='127.0.0.1', port=8000, proxy_headers=True, reload=True)
    #nos establece el entry point y uvicorn recarga en tiempo real con la bandera reload true
