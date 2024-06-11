const extraFeatures = document.querySelectorAll('.adminExtraFeature')
const infoBox = document.querySelector('#infoBox')
// const forms = document.querySelectorAll('.validated-form')
let user = JSON.parse(localStorage.getItem('user'))

displayUserLogin()
showExtraFeaturesIfAdmin()

// UI functions
function displayUserLogin() {
   if (user) {
      document.querySelector('#usernameInfo').textContent = `Hi, ${user.username}`
   }
}

function showExtraFeaturesIfAdmin() {
   for (const extraFeature of extraFeatures) extraFeature.style.display = 'none'

   if (user && user.role === 'admin') {
      for (const extraFeature of extraFeatures) extraFeature.style.display = 'block'
   }
}

function displayInfoBox(message, type) {
   infoBox.textContent = message
   infoBox.classList.remove('alert-success', 'alert-danger', 'alert-info')
   infoBox.classList.add(`alert-${type}`)
   infoBox.classList.remove('d-none')
   setTimeout(() => {
      infoBox.classList.add('d-none')
      infoBox.classList.remove(`alert-${type}`)
   }, 5000)
}

// API
async function callApi(endpoint, method, body) {
   const options = {
      method: method,
      headers: { Accept: 'application/json' },
   }
   if (body) {
      options.headers['Content-Type'] = 'application/json'
      options.body = JSON.stringify(body)
   }
   const response = await fetch(endpoint, options)
   if (response.ok) {
      return await response.json()
   } else {
      const error = await response.json()
      console.log(error.message)
      return null
   }
}
