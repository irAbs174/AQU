function createTable() {
  var tableHTML = `
    <table id="materials-table">
      <thead>
        <tr>
          <th>نام</th>
          <th>نماد</th>
          <th>توضیحات</th>
          <th>موجودی</th>
          <th>قیمت</th>
          <th>واحد</th>
          <th>عملیات</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>
    <table id="total">
    <thead>
      <tr>
        <th id="total-tha">جمع کل</th>
      </tr>
      <tr>
      <th id="total-th">0</th>
    </tr>
    </thead>
    <tbody></tbody>
  </table>
  `;
  document.getElementById('table-container').innerHTML = tableHTML;
  document.getElementById('create-table-btn').style.display = "none";
  document.getElementById('add-row-btn').style.display = "inline-block";
  document.getElementById('save-data-btn').style.display = "inline-block";
}


function addRow(name, simbol, desc, quantity, price, unit) {
  const tableBody = document.getElementById('materials-table').querySelector('tbody');
  const newRow = tableBody.insertRow();

  newRow.innerHTML = `
    <td><input class="cell" type="text" class="material-name" value="${name}" disabled></td>
    <td><input class="cell" type="text" class="material-symbol" value="${simbol}" disabled></td>
    <td><input class="cell" type="text" class="material-description" value="${desc}" disabled></td>
    <td><input class="cell" type="number" class="material-quantity"value="${quantity}" disabled></td>
    <td><input class="cell" type="number" class="material-price" value="${price}" disabled></td>
    <td>
      <select class="material-unit cell">
        <option value="Unit1">${unit}</option>
      </select>
    </td>
    <td><button id="delete-cell" onclick="deleteRow(this)">حذف ماده</button></td>
  `;
    // After inserting the row, calculate the total
    calculateTotal();
}

function deleteRow(btn) {
  btn.closest('tr').remove();
  // After deleting the row, calculate the total
  calculateTotal();
}

function calculateTotal() {
  const rows = document.getElementById('materials-table').querySelectorAll('tbody tr');
  let totalPrice = 0;
  Array.from(rows).forEach(row => {
    const inputs = row.querySelectorAll('input');
    const quantity = parseFloat(inputs[3].value); // Assuming index 3 is the quantity input
    totalPrice += quantity;
  });
  document.getElementById('total-th').textContent = totalPrice; // Display the total in the total cell
}

function saveData() {
  const rows = document.getElementById('materials-table').querySelectorAll('tbody tr');
  const data = Array.from(rows).map(row => {
    const inputs = row.querySelectorAll('input');
    const select = row.querySelector('select');
    return {
      name: inputs[0].value,
      symbol: inputs[1].value,
      description: inputs[2].value,
      quantity: inputs[3].value,
      price: inputs[4].value,
      unit: select.value
    };
  });

  console.log(data);

  let totalPrice = 0;
  Array.from(rows).forEach(row => {
    const inputs = row.querySelectorAll('input');
    const quantity = parseFloat(inputs[3].value);
    const price = parseFloat(inputs[4].value);
    totalPrice += quantity * price;
  });

  const totalData = {
    total: totalPrice
  };
  // Here, you would typically send this data to the server.
  // For example:
  // fetch('api/materials/save', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify(data)
  // })
  // .then(response => response.json())
  // .then(data => console.log(data));
}

function selectMaterial() {
  fetch('materials_list').then(response => {
    if (!response.ok) throw new Error('Network response was not ok.');
    return response.json();
  }).then(materials => {
    let options = materials.map(material =>
      `<option value="${material.material_key}">${material.material_name}</option>`
    ).join('');
    Swal.fire({
      title: 'ماده اولیه را انتخاب کنید',
      html: '<select id="swal-input" class="swal2-input">' + options + '</select>',
      focusConfirm: false,
      confirmButtonText: 'تائید',
      preConfirm: () => {
        const selectedKey = Swal.getPopup().querySelector('#swal-input').value;
        return materials.find(material => material.material_key === selectedKey);
      }
    }).then((result) => {
      if (result.isConfirmed) {
        material_detail_receive(result.value);
      }
    });
  }).catch(error => {
    console.error('Error:', error);
    Swal.fire('خطا', 'درخواست به سرور با مشکل مواجه شد', 'error');
  });
}

function material_detail_receive(selectedMaterial) {
  fetch('material_detail', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ 'material_name': selectedMaterial.material_name }),
  })
  .then(response => response.json())
  .then(response => {
    if (response.success !== false) {
      // Assuming `response` contains the new material data in the expected format
      addRow(
        response.status.material_name,
        response.status.material_key, // Change these keys to match your response data structure
        response.status.material_color,
        10,
        10,
        response.status.material_unit,
      );
    } else {
      Swal.fire('خطا', 'درخواست به سرور با مشکل مواجه شد', 'error');
    }
  }).catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });
}

// Event listener to start the material selection
document.getElementById('create-table-btn').addEventListener('click', function(e) {
  e.preventDefault();
  selectMaterial();
});