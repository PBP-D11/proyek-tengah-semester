$(document).ready(function() {
    $.ajax({
        url: window.jsonUrl,
        type: "GET",
        success: function(result){
          console.log("GET")
          let htmlString = ""
          for (let index = 0; index < result.length; index++) {
              var station = result[index].fields
              htmlString += `<div class="card text-bg-light m-3" style="width:20rem">
                                  <h5 class="card-header">${station.nama_station}</h5>
                                  <div class="card-body">
                                    <p class ="card-text text-black-50">${station.kota}</p>
                                    <p class="card-text">${station.time_open}-${station.time_close}</p>
                                    <p class="card-text">${station.alamat}</p>
                                  </div>
                                  <div class="card-footer">
                                    <a href=${station.link_gmap} class="btn btn-primary" role="button" aria-disabled="false" target="_blank">Google Map</a>
                                    <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#successModal">Check In</button>   
                                  </div>
                              </div>
                              <br>`                  
          }
          $("#stn-card").append(htmlString)
        }
    })

    $("#stn-form").submit(function(e) {
        e.preventDefault()

        $.ajax({
            type: "POST",
            url: `/find-charge/add/`,
            data: $(this).serialize(),
            success: function(response){
              console.log(response)
              let htmlString = ""
              if (response[0].fields.kota === kota) {
                for (let index = 0; index < response.length; index++) {
                  var station = response[index].fields;
                  htmlString += `<div class="card text-bg-light m-3" style="width:20rem">
                                    <h5 class="card-header">${station.nama_station}</h5>
                                    <div class="card-body">
                                      <p class ="card-text text-black-50">${station.kota}</p>
                                      <p class="card-text">${station.time_open}-${station.time_close}</p>
                                      <p class="card-text">${station.alamat}</p>
                                    </div>
                                    <div class="card-footer">
                                      <a href=${station.link_gmap} class="btn btn-primary" role="button" aria-disabled="false" target="_blank">Google Map</a>
                                      <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#successModal">Check In</button>   
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