import gdown

# Google Drive File ID (from shareable link)
file_id = '1GndryS390mCBFbvg6gyOpFpmr1zJxMJZ'
url = f'https://drive.google.com/uc?id={file_id}'

output = 'recommender_app/similarity.pkl'
gdown.download(url, output, quiet=False)