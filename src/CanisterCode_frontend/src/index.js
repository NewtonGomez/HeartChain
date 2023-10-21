import { CanisterCode_backend } from "../../declarations/CanisterCode_backend";
import { Actor, HttpAgent } from '@dfinity/agent';
import { idlFactory as myCanisterIdlFactory, canisterId as myCanisterId } from 'dfx-generated/my_canister';

function mostrarAnalisis() {
  // Abre una ventana emergente con una URL (puede ser una página web o una dirección).
  // El segundo parámetro es el nombre de la ventana (puedes proporcionar "_blank" para abrir una nueva ventana).
  // El tercer parámetro son las opciones de la ventana (como dimensiones, barras de herramientas, etc.).
  // Abre una ventana emergente con contenido personalizado
  const popup = window.open("", "_blank", "width=400,height=400");
  
  // Agrega contenido a la ventana emergente
  //const contenido = '<div class="popup" id="popup"><div class="popup-content"><p>Analizando ECG</p><div class="spinner"></div></div><style>/* Estilos para el botón que abre el popup */button#popupButton {display: block;margin: 20px auto;padding: 10px 20px;background-color: #007BFF;color: #fff;border: none;border-radius: 5px;cursor: pointer;}.popup {display: none;position: fixed;top: 0;left: 0;width: 100%;height: 100%;background: rgba(0, 0, 0, 0.6);}.popup-content {position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);padding: 20px;background: #fff;text-align: center;border-radius: 5px;}.spinner {border: 4px solid rgba(255, 255, 255, 0.3);border-top: 4px solid #007BFF;border-radius: 50%;width: 30px;height: 30px;animation: spin 2s linear infinite;}@keyframes spin {0% { transform: rotate(0deg); }100% { transform: rotate(360deg); }</style></div>';
  const contenido = "<h1>ESTOY ANALIZANDO TU ECG</h1>";
  popup.document.write(contenido);
  popup.document.close();
}

function mostrarMenorEdad() {
  // Abre una ventana emergente con una URL (puede ser una página web o una dirección).
  // El segundo parámetro es el nombre de la ventana (puedes proporcionar "_blank" para abrir una nueva ventana).
  // El tercer parámetro son las opciones de la ventana (como dimensiones, barras de herramientas, etc.).
  // Abre una ventana emergente con contenido personalizado
  const popup = window.open("", "_blank", "width=400,height=400");
  
  // Agrega contenido a la ventana emergente
  //const contenido = '<div class="popup" id="popup"><div class="popup-content"><p>Analizando ECG</p><div class="spinner"></div></div><style>/* Estilos para el botón que abre el popup */button#popupButton {display: block;margin: 20px auto;padding: 10px 20px;background-color: #007BFF;color: #fff;border: none;border-radius: 5px;cursor: pointer;}.popup {display: none;position: fixed;top: 0;left: 0;width: 100%;height: 100%;background: rgba(0, 0, 0, 0.6);}.popup-content {position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);padding: 20px;background: #fff;text-align: center;border-radius: 5px;}.spinner {border: 4px solid rgba(255, 255, 255, 0.3);border-top: 4px solid #007BFF;border-radius: 50%;width: 30px;height: 30px;animation: spin 2s linear infinite;}@keyframes spin {0% { transform: rotate(0deg); }100% { transform: rotate(360deg); }</style></div>';
  const contenido = "<h1>No eres mayor de edad</h1>";
  popup.document.write(contenido);
  popup.document.close();
}

function borrar_Datos() {
    // Borrar el valor del input con id "age"
  document.getElementById("age").value = "";

  // Borrar el valor del input con id "gender"
  document.getElementById("gender").value = "";
}


document.getElementById("myForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const age = document.getElementById("age").value;
  const gender = document.getElementById("gender").value;
  // Aquí puedes realizar acciones adicionales con los datos ingresados.

  
  if (age > 18) {
    mostrarAnalisis();
    borrar_Datos();

    // Crear una instancia del agente HTTP
    const agent = new HttpAgent();
    const canister = Actor.createActor(myCanisterIdlFactory, { agent, canisterId: myCanisterId });
    canister.enviarDatos(edad, sexo).then((respuesta) => {
      var nuevoParrafo = document.createElement("h1");
      nuevoParrafo.textContent = "Con forme a nuestro analisis hemos definido que " + respuesta;
      document.getElementById("ans").appendChild(nuevoParrafo);
    }).catch((error) => {
      console.error(error);
    });
  }else{
    mostrarMenorEdad();
    borrar_Datos();
  }
});