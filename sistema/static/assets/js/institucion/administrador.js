function listadoAdministradores(){
    $.ajax({
        url: "/institucion/listar_administradores/",//se llama al prime nombre listar_administradores
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_administradores')){
                $('#tabla_administradores').DataTable().destroy();
            }
            $('#tabla_administradores tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['apellido'] + '</td>';
                fila += '<td>' + response[i]["fields"]['telefono'] + '</td>';
                fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
                fila += '<td>' + response[i]["fields"]['email'] + '</td>';
                fila += '<td>' + response[i]["fields"]['notificacion'] + '</td>';
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/institucion/editar_administrador/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/institucion/eliminar_administrador/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';
                $('#tabla_administradores tbody').append(fila);
            }             
            $('#tabla_administradores').DataTable({
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
function listadoAdministrador(){
    $.ajax({
        url: "/institucion/estado_administrador/",//se llama al prime nombre listar_administradores
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_administrador')){
                $('#tabla_administrador').DataTable().destroy();
            }
            $('#tabla_administrador tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['apellido'] + '</td>';
                fila += '<td>' + response[i]["fields"]['telefono'] + '</td>';
                fila += '<td>' + response[i]["fields"]['domicilio'] + '</td>';
                fila += '<td>' + response[i]["fields"]['email'] + '</td>';
                fila += '<td>' + response[i]["fields"]['notificacion'] + '</td>';
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/institucion/editar_administrador/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/institucion/eliminar_administrador/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';
                $('#tabla_administrador tbody').append(fila);
            }             
            $('#tabla_administrador').DataTable({
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
            listadoAdministradores();
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
	$.ajax({
		data: $('#form_edicion').serialize(),
		url: $('#form_edicion').attr('action'),
		type: $('#form_edicion').attr('method'),
		success: function(response) {
            notificacionSuccess(response.mensaje);
			listadoAdministradores();
			cerrar_modal_edicion();
		},
		error: function(error) {
            notificacionError(error.responseJSON.mensaje);
			mostrarErroresEdicion(error);
            activarBoton();
		}
	});
}
function eliminar(pk){
	$.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
		url: '/institucion/eliminar_administrador/'+pk+'/',
		type: 'post',
		success: function(response) {
            notificacionSuccess(response.mensaje);
			listadoAdministradores();
			cerrar_modal_eliminacion();
		},
		error: function(error) {
            notificacionError(error.responseJSON.mensaje);
		}
	});
}
$(document).ready(function(){
    listadoAdministradores();
    listadoAdministrador();
});