

/**
 * Get data from api to display in activities page
 */

showLoading();
fetch('/api/activities')
.then(res => res.json())
.then(data => {
    console.log(data);
    getDisplayArray(data);
    hideLoading();
})
.catch(err => console.log(err));

let displayArray = []
function getDisplayArray(data) {
    for (i = 0; i < 12; i++){
        displayArray.push(data[i]);
    }
    console.log(displayArray);
}


