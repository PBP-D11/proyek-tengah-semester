function useAlert() {
  const toast = new bootstrap.Toast($('#toastAlert')[0])
  toast.show()
}

function useSuccess() {
  const toast = new bootstrap.Toast($('#toastSuccess')[0])
  toast.show()
}

hapusCar = (idCar) => {
  $.ajax({
    url :`/wishlist/delete/${idCar}`,
    type : 'DELETE',
    succes:function(response){
      $(`#${idCar}--car`).remove()
    }
  })
}

parseDate = (d) => {
  let date = new Date(d);        
  var mm = date.getMonth() + 1; // getMonth() adalah zero-based
  var dd = date.getDate();

  let newdate = [date.getFullYear() + '-',
                (mm>9 ? '' : '0') + mm + '-',
                (dd>9 ? '' : '0') + dd,
                ].join('');
  return newdate;
}

function cardCar(id){
  $('#wishlist').prepend(
    `<div id = "${id.pk}--car" class = "rounded-lg pl-6 pr-6 py-5 bg-black shadow-md hover:shadow-xl">
        <div>
                <h1 id = "${id.pk}--name" class = "text-lg font-bold">${id.fields.name}</h1>
                <p id = "${id.pk}--price" class="text-abu-muda text-base mb-4">${id.fields.price}</p>
        </div>
    </div>`);
}