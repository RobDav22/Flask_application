const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Quieres eliminar este contacto?')) {
                e.preventDefault();
            }
        });
    });
}