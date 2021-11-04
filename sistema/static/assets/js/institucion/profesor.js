function listadoProfesores(){
    $.ajax({
        url: "/institucion/listar_profesores/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_profesores')){
                $('#tabla_profesores').DataTable().destroy();
            }
            $('#tabla_profesores tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['dni'] + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['apellido'] + '</td>';
                fila += '<td>' + response[i]["fields"]['email'] + '</td>';
                fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
                fila += '<td>' + response[i]["fields"]['telefono'] + '</td>'; 
                fila += '<td>' + response[i]["fields"]['notificacion'] + '</td>';                      
                fila += '<td> <button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/institucion/editar_profesor/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton btn-sm"';
                fila += 'onclick = "abrir_modal_eliminacion(\'/institucion/eliminar_profesor/'+ response[i]['pk']+'/\');"> ELIMINAR </button> </td>';
                fila += '</tr>';
                $('#tabla_profesores tbody').append(fila);
            }             
            $('#tabla_profesores').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                      "first": "Primero",
                      "last": "Ultimo",
                      "next": "Siguiente",
                      "previous": "Anterior"
                    },
                  },
            });
        },
        error: function(error){
            console.log(error);
        }
    });
}
function listadoProfesor(){
    $.ajax({
        url: "/institucion/estado_profesor/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_profesor')){
                $('#tabla_profesor').DataTable().destroy();
            }
            $('#tabla_profesor tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['dni'] + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['apellido'] + '</td>';
                fila += '<td>' + response[i]["fields"]['email'] + '</td>';
                fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
                fila += '<td>' + response[i]["fields"]['telefono'] + '</td>'; 
                fila += '<td>' + response[i]["fields"]['notificacion'] + '</td>';                      
                fila += '<td> <button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/institucion/editar_profesor/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton btn-sm"';
                fila += 'onclick = "abrir_modal_eliminacion(\'/institucion/eliminar_profesor/'+ response[i]['pk']+'/\');"> ELIMINAR </button> </td>';
                fila += '</tr>';
                $('#tabla_profesor tbody').append(fila);
            }             
            $('#tabla_profesor').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                      "first": "Primero",
                      "last": "Ultimo",
                      "next": "Siguiente",
                      "previous": "Anterior"
                    },
                  },
            });
        },
        error: function(error){
            console.log(error);
        }
    });
}
function registrar() {
    activarBoton();
    var data = new FormData($('#form_creacion').get(0));
    $.ajax({        
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'), 
        data: data,
        cache: false,
        processData: false,
        contentType: false, 
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoProfesores();
            cerrar_modal_creacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}
function editar() {
    activarBoton();
    var data = new FormData($('#form_edicion').get(0));
    $.ajax({        
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'), 
        data: data,
        cache: false,
        processData: false,
        contentType: false, 
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoProfesores();
            cerrar_modal_edicion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        },        
    });
}
function eliminar(pk){
	$.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
		url: '/institucion/profesor/eliminar_profesor/'+pk+'/',
		type: 'post',
		success: function(response) {
            notificacionSuccess(response.mensaje);
			listadolistadoProfesoresLibros();
			cerrar_modal_eliminacion();
		},
		error: function(error) {
            notificacionError(error.responseJSON.mensaje);
		}
	});
}
$(document).ready(function(){
    listadoProfesores();
    listadoProfesor();
});