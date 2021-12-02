function listadoInscripciones(){
    $.ajax({
        url: "/institucion/listar_inscripciones/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_inscripciones')){
                $('#tabla_inscripciones').DataTable().destroy();
            }
            $('#tabla_inscripciones tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['fecha_inscripcion'] + '</td>';
                if (response[i]["fields"]['id_alumno'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_alumno'] + '</td>';       
                }
                if (response[i]["fields"]['id_materia'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_materia'] + '</td>';       
                }
                fila += '<td> <button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/institucion/editar_inscripcion/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton btn-sm"';
                fila += 'onclick = "abrir_modal_eliminacion(\'/institucion/eliminar_inscripcion/'+ response[i]['pk']+'/\');"> ELIMINAR </button>';
                fila += '<button type = "button" class = "btn btn-info tableButton btn-sm"';
                fila += 'onclick="location.href=(\'/institucion/detalle_inscripcion/'+ response[i]['pk']+'/\');"> DETALLE </button> </td>';
                fila += '</tr>';
                $('#tabla_inscripciones tbody').append(fila);
            }             
            $('#tabla_inscripciones').DataTable({
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

function listado(){
    $.ajax({
        url: "/institucion/listar_inscripciones/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_mya')){
                $('#tabla_mya').DataTable().destroy();
            }
            $('#tabla_mya tbody').html("");
            for(let i = 0;i < response.length;i++){
                if (response[i]["fields"]['id_materia'] == 'programacion 1'){
                   
                    let fila = '<tr>';
                    if (response[i]["fields"]['id_materia'] == ''){
                        fila += '<td> Desconocido </td>';
                    } else {
                        fila += '<td>' + response[i]["fields"]['id_materia'] + '</td>';       
                    }
                    if (response[i]["fields"]['id_alumno'] == ''){
                        fila += '<td> Desconocido </td>';
                    } else {
                        fila += '<td>' + response[i]["fields"]['id_alumno'] + '</td>';       
                    }
                    
                    fila += '<td> <button type = "button" class = "btn btn-primary btn-sm tableButton"';
                    fila += ' onclick = "abrir_modal_edicion(\'/institucion/editar_inscripcion/' + response[i]['pk']+'/\');"> EDITAR </button>';
                    fila += '<button type = "button" class = "btn btn-danger tableButton btn-sm"';
                    fila += 'onclick = "abrir_modal_eliminacion(\'/institucion/eliminar_inscripcion/'+ response[i]['pk']+'/\');"> ELIMINAR </button> </td>';
                    fila += '</tr>';
                    $('#tabla_mya tbody').append(fila);
                }
            }             
            $('#tabla_mya').DataTable({
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
            listadoInscripciones();
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
            listadoInscripciones();
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
		url: '/institucion/eliminar_inscripcion/'+pk+'/',
		type: 'post',
		success: function(response) {
            notificacionSuccess(response.mensaje);
			listadoInscripciones();
			cerrar_modal_eliminacion();
		},
		error: function(error) {
            notificacionError(error.responseJSON.mensaje);
		}
	});
}
$(document).ready(function(){
    listadoInscripciones();
});