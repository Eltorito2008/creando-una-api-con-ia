class Concesionario {
    constructor() {
        this.autos = JSON.parse(localStorage.getItem('concesionarioAutos')) || [];
        this.autoEditando = null;
        this.init();
    }

    init() {
        this.renderizarInventario();
        this.setupEventListeners();
    }

    setupEventListeners() {
        document.getElementById('autoForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.guardarAuto();
        });

        document.getElementById('cancelBtn').addEventListener('click', () => {
            this.cancelarEdicion();
        });

        document.getElementById('searchInput').addEventListener('input', (e) => {
            this.buscarAutos(e.target.value);
        });
    }

    guardarAuto() {
        const formData = new FormData(document.getElementById('autoForm'));
        const autoData = {
            id: this.autoEditando ? this.autoEditando : this.generarId(),
            marca: document.getElementById('marca').value,
            modelo: document.getElementById('modelo').value,
            anio: parseInt(document.getElementById('anio').value),
            precio: parseFloat(document.getElementById('precio').value),
            color: document.getElementById('color').value
        };

        if (this.autoEditando) {
            const index = this.autos.findIndex(auto => auto.id === this.autoEditando);
            this.autos[index] = autoData;
        } else {
            this.autos.push(autoData);
        }

        this.guardarEnLocalStorage();
        this.renderizarInventario();
        this.limpiarFormulario();
    }

    editarAuto(id) {
        const auto = this.autos.find(auto => auto.id === id);
        if (auto) {
            document.getElementById('autoId').value = auto.id;
            document.getElementById('marca').value = auto.marca;
            document.getElementById('modelo').value = auto.modelo;
            document.getElementById('anio').value = auto.anio;
            document.getElementById('precio').value = auto.precio;
            document.getElementById('color').value = auto.color;
            
            this.autoEditando = id;
            document.querySelector('button[type="submit"]').textContent = 'Actualizar Auto';
        }
    }

    eliminarAuto(id) {
        if (confirm('¿Estás seguro de que quieres eliminar este auto?')) {
            this.autos = this.autos.filter(auto => auto.id !== id);
            this.guardarEnLocalStorage();
            this.renderizarInventario();
        }
    }

    cancelarEdicion() {
        this.limpiarFormulario();
        this.autoEditando = null;
        document.querySelector('button[type="submit"]').textContent = 'Guardar Auto';
    }

    limpiarFormulario() {
        document.getElementById('autoForm').reset();
        document.getElementById('autoId').value = '';
    }

    buscarAutos(termino) {
        const autosFiltrados = this.autos.filter(auto => 
            auto.marca.toLowerCase().includes(termino.toLowerCase()) ||
            auto.modelo.toLowerCase().includes(termino.toLowerCase()) ||
            auto.color.toLowerCase().includes(termino.toLowerCase()) ||
            auto.anio.toString().includes(termino)
        );
        this.renderizarInventario(autosFiltrados);
    }

    renderizarInventario(autos = this.autos) {
        const inventoryList = document.getElementById('inventoryList');
        
        if (autos.length === 0) {
            inventoryList.innerHTML = '<p class="no-autos">No hay autos en el inventario.</p>';
            return;
        }

        inventoryList.innerHTML = autos.map(auto => `
            <div class="auto-card">
                <div class="auto-info">
                    <h3>${auto.marca} ${auto.modelo}</h3>
                    <div class="auto-details">
                        <strong>Año:</strong> ${auto.anio} | 
                        <strong>Color:</strong> ${auto.color} | 
                        <strong>Precio:</strong> $${auto.precio.toLocaleString()}
                    </div>
                </div>
                <div class="auto-actions">
                    <button class="btn-edit" onclick="concesionario.editarAuto('${auto.id}')">Editar</button>
                    <button class="btn-delete" onclick="concesionario.eliminarAuto('${auto.id}')">Eliminar</button>
                </div>
            </div>
        `).join('');
    }

    guardarEnLocalStorage() {
        localStorage.setItem('concesionarioAutos', JSON.stringify(this.autos));
    }

    generarId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }
}

// Inicializar la aplicación
const concesionario = new Concesionario();