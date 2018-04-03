set -e
# If no dir, create it
mkdir -p proto/mocks/img
mkdir -p media/proto/gallery
MEDIA=media/proto/gallery/
MEDIA_COUNT=$(ls -1 $MEDIA | wc -l)
if [ $MEDIA_COUNT = "0" ]; then
  # If empty download an image into
  IMG_MOCKS=proto/mocks/img/
  IMG_MOCKS_COUNT=$(ls -1 $IMG_MOCKS | wc -l)
  if [ $IMG_MOCKS_COUNT = "0" ]; then
    sudo apt-get install unzip
    wget http://static.onit.ws/tathros/mockedImages.zip
    unzip mockedImages.zip -d proto/mocks/img/
  fi
  rm -rf mockedImages.zip
fi
echo 'IMPORTING MOCKS'
python manage.py importmocks 3 true
