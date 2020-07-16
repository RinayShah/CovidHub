function readUrlInput(e) {
    const element = document.getElementById('input-url');
    imageUrl = element.value;
    const imageContainerElem = document.getElementById("image-container");
    imageElem = document.createElement("IMG");
    imageElem.src = imageUrl;
    imageElem.alt = "Unknown Image";
    imageContainerElem.removeChild(imageContainerElem.childNodes[0]);
    if (imageContainerElem.childNodes.length > 0) {
        imageContainerElem.removeChild(imageContainerElem.childNodes[0]);
        imageContainerElem.appendChild(imageElem);
    }
     else {
        imageContainerElem.appendChild(imageElem);
    }
    watsonServiceUrl = "http://think-fyre-covid-hub-watson-service.us-east.mybluemix.net/visual/recognizer"
    payload = {"image_url": imageUrl};
    postData(watsonServiceUrl, payload)
    .then(response => {
        response.json().then(data => {
            dataJSON = data;
            document.getElementById('surface-name').innerHTML = capitalizeFirstLetter(dataJSON.surface_name);
            document.getElementById('life-time').innerHTML = "Duration: " + dataJSON.life_time;
            document.getElementById('action-details').innerHTML = "Take Action: " + dataJSON.advice;
          });
    });
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      return response;

  }
  

document.getElementById('analyze-button')
  .addEventListener('click', readUrlInput, false);