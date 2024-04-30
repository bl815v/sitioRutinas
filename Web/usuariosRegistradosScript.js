
function editarUsuario(idUsuario) {
    document.getElementById('bEditar').style.display = 'none';
    var filaUsuario = document.getElementById('fila_' + idUsuario);
    var filaEdicion = document.createElement('tr');
    filaUsuario.parentNode.insertBefore(filaEdicion, filaUsuario.nextSibling);
    filaEdicion.innerHTML = `<td colspan="11">
                                <input type="text" id="nombre_${idUsuario}" value="${filaUsuario.cells[1].innerText}">
                                <input type="text" id="documento_${idUsuario}" value="${filaUsuario.cells[2].innerText}">
                                <input type="text" id="celular_${idUsuario}" value="${filaUsuario.cells[3].innerText}">
                                <input type="text" id="correo_${idUsuario}" value="${filaUsuario.cells[4].innerText}">
                                <input type="text" id="altura_${idUsuario}" value="${filaUsuario.cells[5].innerText}">
                                <input type="text" id="peso_${idUsuario}" value="${filaUsuario.cells[6].innerText}">
                                <input type="text" id="dias_${idUsuario}" value="${filaUsuario.cells[7].innerText}">
                                <input type="text" id="objetivo_${idUsuario}" value="${filaUsuario.cells[8].innerText}">
                                <button onclick="guardarEdicion(${idUsuario})">Guardar</button>
                              </td>`;
}


function guardarEdicion(idUsuario) {
    var nombre = document.getElementById('nombre_' + idUsuario).value;
    var documento = document.getElementById('documento_' + idUsuario).value;
    var celular = document.getElementById('celular_' + idUsuario).value;
    var correo = document.getElementById('correo_' + idUsuario).value;
    var altura = document.getElementById('altura_' + idUsuario).value;
    var peso = document.getElementById('peso_' + idUsuario).value;
    var dias = document.getElementById('dias_' + idUsuario).value.split(',').map(day => day.trim());
    var objetivo = document.getElementById('objetivo_' + idUsuario).value;

    fetch(`/actualizarUsuario/${idUsuario}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nombre: nombre,
            documento: documento,
            celular: celular,
            correo: correo,
            altura: altura,
            peso: peso,
            dias: dias,
            objetivo: objetivo
        })
    }).then(response => {
        if (response.ok) {
            var filaEdicion = document.getElementById('fila_' + idUsuario).nextSibling;
            filaEdicion.parentNode.removeChild(filaEdicion);
            location.reload();
        } else {
            console.error('Error al actualizar el usuario');
        }
    }).catch(error => {
        console.error('Error de red:', error);
    });
}
