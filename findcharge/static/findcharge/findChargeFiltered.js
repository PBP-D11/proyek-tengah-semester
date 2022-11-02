$(document).ready(function() {
    // Get data from json and append data
    $.ajax({
        url: window.jsonUrl,
        type: "GET",
        success: function(result){
          let htmlString = ""
          for (let index = 0; index < result.length; index++) {
              var station = result[index].fields
              htmlString += `<div class="card text-bg-light m-3" style="width:20rem">
                                <img src="https://maps.gstatic.com/tactile/pane/default_geocode-2x.png">
                                <div class="card-body">
                                  <h5 class="card-title">${station.nama_station}</h5>
                                  <p class ="card-text text-black-50">${station.kota}</p>
                                </div>
                                <ul class="list-group list-group-flush">
                                  <li class="list-group-item">${station.time_open}-${station.time_close}</li>
                                  <li class="list-group-item">${station.alamat}</li>
                                </ul>
                                <div class="card-footer">
                                  <a href=${station.link_gmap} class="btn btn-primary" role="button" aria-disabled="false" target="_blank">Google Map</a>
                                  <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#successModal" onclick="addHistory(${result[index].pk})">Check In</button>   
                                </div>
                            </div>
                            <br>`                 
          }
          $("#stn-card").append(htmlString)
        }
    })
    
    // Get new data and append
    $("#stn-form").submit(function(e) {
        e.preventDefault()

        $.ajax({
            type: "POST",
            url: `/find-charge/add/`,
            data: $(this).serialize(),
            success: function(response){
              let htmlString = ""
              if (response[0].fields.kota === kota) {
                for (let index = 0; index < response.length; index++) {
                  var station = response[index].fields;
                  htmlString += `<div class="card text-bg-light m-3" style="width:20rem">
                                  <img src="https://maps.gstatic.com/tactile/pane/default_geocode-2x.png">
                                  <div class="card-body">
                                    <h5 class="card-title">${station.nama_station}</h5>
                                    <p class ="card-text text-black-50">${station.kota}</p>
                                    <p class="card-text">${station.time_open}-${station.time_close}</p>
                                    <p class="card-text">${station.alamat}</p>
                                  </div>
                                  <ul class="list-group list-group-flush">
                                    <li class="list-group-item">${station.time_open}-${station.time_close}</li>
                                    <li class="list-group-item">${station.alamat}</li>
                                  </ul>
                                  <div class="card-footer">
                                    <a href=${station.link_gmap} class="btn btn-primary" role="button" aria-disabled="false" target="_blank">Google Map</a>
                                    <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#successModal" onclick="addHistory(${response[index].pk})">Check In</button>   
                                  </div>
                              </div>
                              <br>`       
                }
              }
              $("#stn-card").append(htmlString)
            }

        })
        $("#stn-form").trigger('reset')
    })
})

let isLoggedIn = window.user

// Add history
function addHistory(pk) {
  if (isLoggedIn != "None") {
    fetch(`/find-charge/checkin/${pk}`)
    return false
  }else {
    location.replace("/login/")
  }
}