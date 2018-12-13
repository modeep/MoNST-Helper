import requests

url = 'http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat'
r = requests.get(url, allow_redirects=True)
open('imagenet-vgg-verydeep-19.mat', 'wb').write(r.content)
