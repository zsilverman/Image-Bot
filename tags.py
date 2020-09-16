from clarifai.rest import ClarifaiApp


app = ClarifaiApp()


def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])

    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])

    return tag_urls