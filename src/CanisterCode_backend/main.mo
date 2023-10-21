import Http "mo:base/Http";
actor {

public func enviarDatos(edad : Text, sexo : Text) : async Text {
  let url = "http://localhost:5000/procesar_datos";
  let cuerpo = Http.encodeFormData({ "edad" : edad, "sexo" : sexo });
  
  let respuesta = await Http.post(url, cuerpo);
  
  if (HttpResponse.isSuccess(respuesta)) {
    return HttpResponse.body(respuesta);
  } else {
    return "Error al enviar los datos";
  }
}
};