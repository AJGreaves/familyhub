

/**
 * Get data from api to display in activities page
 */

showLoading();
fetch('/api/activities')
.then(res => res.json())
.then(data => {
    console.log(data)
    hideLoading();
})
.catch(err => console.log(err));



