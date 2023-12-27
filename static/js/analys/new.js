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
          <tbody>
              <tr>
                  <td><input type="text" class="نام ماده"></td>
                  <td><input type="text" class="رنگ"></td>
                  <td><input type="text" class="واحد"></td>
                  <td><input type="number" class="نرخ" value="0"></td>
                  <td><input type="number" class="تاریخ نرخ گذاری" value="0"></td>
                  <td>
                      <select class="unit">
                          <option value="Unit1">متر</option>
                          <option value="Unit2">عدد</option>
                      </select>
                  </td>
                  <td><button onclick="deleteRow(this)">حذف ماده</button></td>
              </tr>
          </tbody>
      </table>
      <button onclick="addRow()">افزودن ماده اولیه جدید</button>
      <button onclick="saveData()">ذخیره</button>
  `;
  document.getElementById('table-container').innerHTML = tableHTML;
  document.getElementById('create-table-btn').style.display = "none"; // Hide the create button
  document.getElementById('add-row-btn').style.display = "inline-block"; // Show add row button
  document.getElementById('save-data-btn').style.display = "inline-block"; // Show save button
  document.getElementById('add-row-btn').disabled = false; // Enable the add row button
  document.getElementById('save-data-btn').disabled = false; // Enable the save button
}

function addRow(name, color, unit) {
    const table = document.getElementById('materials-table').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow(table.rows.length);
    const columns = ['نام', 'نماد', 'توضیحات', 'موجودی', 'قیمت', 'واحد', 'action'];

    columns.forEach((col, index) => {
      const cell = newRow.insertCell(index);
      if (col === 'unit') {
        const select = document.createElement('select');
        select.classList.add('unit');
        const units = [unit]; // Replace with your list of units from Django
        units.forEach(unit => {
          select.appendChild(units);
        });
        cell.appendChild(select);
      } else if (col === 'action') {
        const button = document.createElement('button');
        button.textContent = 'حذف ماده';
        button.onclick = function() {
          deleteRow(this);
        };
        cell.appendChild(button);
      } else {
        const input = document.createElement('input');
        input.type = col === 'quantity' || col === 'price' ? 'number' : 'text';
        input.classList.add(col);
        input.value = col === 'quantity' || col === 'price' ? 0 : '';
        cell.appendChild(input);
      }
    });
  }

  function deleteRow(btn) {
    const row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
  }

  function saveData() {
    const table = document.getElementById('materials-table');
    const rows = table.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
    const data = [];

    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName('td');
      const rowData = {};
      for (let j = 0; j < cells.length - 1; j++) {
        const cell = cells[j].querySelector('input, select');
        rowData[cell.classList[0]] = cell.value;
      }
      data.push(rowData);
    }

    console.log(data);
    // Add logic to handle the data (e.g., sending it to a server, etc.)
  }

  function selectMaterial() {
    // Make a request to the server to get the materials
    fetch('materials_list')   // Make sure 'api/materials/' is the correct endpoint exposed by your Django server to get materials
      .then(response => {
        if (response.ok) {
          return response.json(); // Convert the response to JSON
        }
        throw new Error('Network response was not ok.');
      })
      .then(materials => {
        // Create the select box options based on the materials received
        let options = materials.map(material =>
          `<option value="${material.material_key}">${material.material_name}</option>`
        ).join('');
    
        // Show the SweetAlert with dynamically created select box options
        Swal.fire({
          title: 'ماده اولیه را انتخاب کنید',
          html: '<select id="swal-input" class="swal2-input">' + options + '</select>',
          focusConfirm: false,
          confirmButtonText: 'تائید',
          preConfirm: () => {
            const selectedKey = document.getElementById('swal-input').value;
            return materials.find(material => material.material_key === selectedKey).material_name;
          }
        }).then((result) => {
          if (result.isConfirmed) {
            // Handle the result of the selection here
            material_detail_recive(result.value);
          }
        });
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
        Swal.fire('خطا', 'درخواست به سرور با مشکل مواجه شد', 'error');
      });
  }

  function selectMaterial_first() {
    // Make a request to the server to get the materials
    fetch('materials_list')   // Make sure 'api/materials/' is the correct endpoint exposed by your Django server to get materials
      .then(response => {
        if (response.ok) {
          return response.json(); // Convert the response to JSON
        }
        throw new Error('Network response was not ok.');
      })
      .then(materials => {
        // Create the select box options based on the materials received
        let options = materials.map(material =>
          `<option value="${material.material_key}">${material.material_name}</option>`
        ).join('');
    
        // Show the SweetAlert with dynamically created select box options
        Swal.fire({
          title: 'ماده اولیه را انتخاب کنید',
          html: '<select id="swal-input" class="swal2-input">' + options + '</select>',
          focusConfirm: false,
          confirmButtonText: 'تائید',
          preConfirm: () => {
            const selectedKey = document.getElementById('swal-input').value;
            return materials.find(material => material.material_key === selectedKey).material_name;
          }
        }).then((result) => {
          if (result.isConfirmed) {
            // Handle the result of the selection here
            createTable()
            material_detail_recive(result.value);
          }
        });
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
        Swal.fire('خطا', 'درخواست به سرور با مشکل مواجه شد', 'error');
      });
  }

  // This function send request to server for give all detail about selected material
  function material_detail_recive(material_name){
    $.ajax({
      url: 'material_detail',
      type: 'POST',
      data: {
        'material_name': material_name,
      },
      success: function (response) {
        if (response.success != false) {
          addRow(response.status.material_name, response.status.material_color, response.status.material_unit);
        }else{
          Swal.fire('خطا', 'درخواست به سرور با مشکل مواجه شد', 'error');
        };// end if
      }
    }); // end AJAX
  };

  $('.start_select_material').click(function (e) {
    e.preventDefault();
    selectMaterial_first();
  }); //end default filter