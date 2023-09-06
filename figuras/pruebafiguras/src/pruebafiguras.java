
public class pruebafiguras {

    public static void main(String[] args) {
        Circulo figura1 = new Circulo(2);
        Rectangulo figura2 = new Rectangulo(1,2);
        Cuadrado figura3= new Cuadrado(3);
        TrianguloR figura4 = new TrianguloR(3,5);
        System.out.println("El area de circulo es " + figura1.calcularArea());
        System.out.println("El perimetro de circulo es " + figura1.calcularPerimetro());
        System.out.println();
        System.out.println("El area de rectangulo es " + figura2.calcularArea());
        System.out.println("El perimetro de rectangulo es " + figura2.calcularPerimetro());
        System.out.println();
        System.out.println("El area de cuadrado es " + figura3.calcularArea());
        System.out.println("El perimetro de cuadrado es " + figura3.calcularPerimetro());
        System.out.println();
        System.out.println("El area de  Triangulo es " + figura4.calcularArea());
        System.out.println("El perimetro de  Triangulo es " + figura4.calcularPerimetro());
        figura4.determinarTipo();
        
 
    
    
    
    
    
    
    }
    
}
