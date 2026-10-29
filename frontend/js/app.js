
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const escena = new THREE.Scene();

const camara = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

camara.position.z = 5;

const renderizador = new THREE.WebGLRenderer();

renderizador.setSize(
    window.innerWidth,
    window.innerHeight
);

document.querySelector(".escenario").appendChild(renderizador.domElement);

const luzAmbiental = new THREE.AmbientLight(0xffffff, 0.5);
escena.add(luzAmbiental);

const luzPrincipal = new THREE.DirectionalLight(0xffffff, 3);
luzPrincipal.position.set(-3, 5, 5);
escena.add(luzPrincipal);

let balon;

const cargador = new GLTFLoader();

cargador.load('/models/basketball.glb', (gltf) => {

    console.log("Modelo cargado correctamente");

    balon = gltf.scene;
    balon.scale.set(20, 20, 20);
    balon.position.set(2.3, 0, 0);
    balon.rotation.z = Math.PI / 2;
    escena.add(balon);

    function animar() {
    requestAnimationFrame(animar);
    renderizador.render(escena, camara);

    // balon.rotation.x += 0.010;

    renderizador.render(escena, camara);
 }

    animar();

    renderizador.render(escena, camara);

});

window.addEventListener("wheel", (evento) => {
    if (balon) {
        balon.rotation.x += evento.deltaY * 0.001;
    }
});