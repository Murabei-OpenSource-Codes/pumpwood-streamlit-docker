source version
git add ./*
git commit -m "Building a new version for Pumpwood Streamlit Base Docker Image ${VERSION}"
git tag -a ${VERSION} -m "Building a new version for Pumpwood Base Docker Image ${VERSION}"
git push
git push origin ${VERSION}

docker push andrebaceti/pumpwood-streamlit-app:${VERSION}
