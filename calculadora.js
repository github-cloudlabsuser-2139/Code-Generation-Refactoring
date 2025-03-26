class Calculadora {
    // Método para sumar
    suma(num1, num2) {
        return num1 + num2;
    }

    // Método para restar
    resta(num1, num2) {
        return num1 - num2;
    }

    // Método para multiplicar
    multiplicacion(num1, num2) {
        return num1 * num2;
    }

    // Método para dividir con validación por cero
    division(num1, num2) {
        if (num2 === 0) {
            return "Error: No se puede dividir por cero.";
        }
        return num1 / num2;
    }
}

// Ejemplo de uso
const calculadora = new Calculadora();

const num1 = 10;
const num2 = 0;

console.log(`Suma: ${calculadora.suma(num1, num2)}`);
console.log(`Resta: ${calculadora.resta(num1, num2)}`);
console.log(`Multiplicación: ${calculadora.multiplicacion(num1, num2)}`);
console.log(`División: ${calculadora.division(num1, num2)}`);