const $formularioCurso = document.getElementById('formularioCurso');
const $txtNombre = document.getElementById('txtNombre');
const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

(function(){

    $formularioCurso.addEventListener('submit', (e) => {
        let nombre = String($txtNombre.value).trim();
        let creditos = String($txtCreditos.value).trim();
        if(nombre.length === 0){
            notificacionSwal(document.title, "El nombre del curso no puede estar vacío", "warning","Ok")
            e.preventDefault();
        }else{
            let creditos = parseInt(creditos.value)
            if(creditos<1 || creditos>10){
                notificacionSwal(document.title, "Los creditos del curso no pueden ser menor de 1 o mayores de 10", "warning","Ok")
                e.preventDefault();
            }
        }

    })

    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            Swal.fire({
                title: "¿Estás seguro de eliminar el curso?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: (result) => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: ()=> false,
            })
        })
    })
    
})()