// $(document).ready(function(){
//     loadData();
//     $('#add-car').click(function () {
//         $.post(
//             '/wishlist/add/',
//             {
//                 name: $('#name').val(),
//                 price: $('#price').val(),
//             },
//             function (data, status) {
//                 if (status == 'success') {
//                     $(`#quest`).prepend(carCard(data))
//                     $('#name').val('')
//                     $('#price').val('')
//                     const toast = new bootstrap.Toast($('#liveToast2'))
//                     toast.show()

//                 }
//             },
//         )
//     })
// });



function useToast() {
    const toast = new bootstrap.Toast($('#liveToast')[0])
    toast.show()
}


function deleteCar(id) {
    $.ajax({
        url: `/wishlist/delete/${id}`,
        type: 'DELETE',
        success: function (result) {
            $(`#quest-${id}`).addClass("animate-scale-down-center")
            setTimeout(function () { $(`#quest-${id}`).remove(); }, 225)
        },
        error: function useToast() {
            const toast = new bootstrap.Toast($('#liveToast'))
            toast.show()
        }
    });
}



async function loadData() {
    await $.get(`/wishlist/json`, function (data) {
        for (var i = 0; i < data.length; i++) {
            $(`#quest`).append(carCard(data[i]));
        }
    });
    $.get(`/wishlist/json2`, function (data) {
        for (var i = 0; i < data.length; i++) {
            $(`#no-answer-${data[i].fields.car}`).text('')
            $(`#quest-reviews-${data[i].fields.car}`).append(answerCard(data[i]));
        }
    });
}

function loveCar(id) {
    $.ajax({
        url: `/wishlist/love/${id}`,
        type: 'PATCH',
        success: function (data) {
            $(`#total-loves-${id}`).text(data.total_love)
        }
    });
}

function cardCar(id) {
    $('#wishlist').prepend(
      `<div id = "${id.pk}--tugas" class = "rounded-lg pl-6 pr-6 py-5 bg-black shadow-md hover:shadow-xl">
        <div>
          <h1 class = "font-semibold text-grey text-sm">${parseDate(id.fields.name)}</h1>
          <h1 id = "${id.pk}--name0" class = "text-lg font-bold">${id.fields.price}</h1>
        </div>
      </div>`);
  
    $('#wishlist').prepend(
      `<!-- Modal Car -->
      <div class="modal fade" id="modalTambah--${id.pk}" tabindex="-1" role="dialog" aria-labelledby="createCarModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg modalCenter">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class = "font-semibold text-grey text-sm">${parseDate(id.fields.date)}</h1>
              <h5 id = "${id.pk}--name1" class="modal-name text-black font-bold" id="createCarModalLabel">${id.fields.name}</h5>
            </div>
            <div class="modal-body">
              <p id = "${id.pk}--price1" class="text-merah-muda font-semibold text-base mb-4">
                ${id.fields.price}
              </p>
            </div>
            <div class="modal-footer">
              <button type="button" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" data-bs-dismiss="modal">Tutup</button>
            </div>
          </div>
        </div>
      </div>`
    );
  }