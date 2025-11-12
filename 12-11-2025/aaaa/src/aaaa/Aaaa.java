/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aaaa;

/**
 *
 * @author estudiante
 */
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import com.google.gson.Gson;
import java.nio.file.Paths;
import java.nio.file.Files;


class Persona{
    public String nombre;
    public String direccion;
    public Persona(String nombre, String direccion){
        this.nombre=nombre;
        this.direccion=direccion;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", direccion=" + direccion + '}';
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
}

public class Aaaa {
    public static void main(String[] args) {
        // TODO code application logic here
        try{
            Gson gson=new Gson();
            
            Persona persona1=new Persona("Axel","aaaa");
            String cadena=gson.toJson(persona1);
            
            FileWriter archivo = new FileWriter("persona.json");
            archivo.write(cadena);
            archivo.close();
            
            Reader archivo2=Files.newBufferedReader(Paths.get("persona.json"));
            Persona persona2=gson.fromJson(archivo2,Persona.class);
            System.out.println(persona2);
            archivo2.close();
            
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
