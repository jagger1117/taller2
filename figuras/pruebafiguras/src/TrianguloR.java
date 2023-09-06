
public class TrianguloR {
    
    int base;
    int altura;
    
    TrianguloR(int base, int altura ){
        this.base=base;
        this.altura=altura;
    }
    double calcularArea(){
        return base*altura;
        
    }
    
    
     double calcularHipotenusa(){
        return Math.pow(((altura*altura)+(base*base)), 0.5);
        
    }
    double calcularPerimetro(){
        return (base+altura+calcularHipotenusa());       
    }
    
    void determinarTipo() {
if ((base == altura) && (base == calcularHipotenusa()) && (altura 
== calcularHipotenusa()))
    System.out.println("Es un triángulo equilátero"); 
else if
    ((base != altura) && (base != calcularHipotenusa()) &&
    (altura != calcularHipotenusa()))
    System.out.println("Es un triangulo escaleno");
else
    System.out.println("Es un triangulo isósceles"); 
}
   
    
}
