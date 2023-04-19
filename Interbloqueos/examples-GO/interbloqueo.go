package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	// Inicializar los recursos
	var (
		A, B sync.Mutex
		wg   sync.WaitGroup
	)

	// Goroutine 1
	wg.Add(1)
	go func() {
		fmt.Println("Goroutine 1 quiere adquirir recurso A")
		A.Lock()
		fmt.Println("Goroutine 1 adquirió recurso A")
		fmt.Println("Goroutine 1 quiere adquirir recurso B")
		// Simular un retraso de 1 segundo
		time.Sleep(1 * time.Second)
		B.Lock()
		fmt.Println("Goroutine 1 adquirió recurso B")
		B.Unlock()
		A.Unlock()
		wg.Done()
	}()

	// Goroutine 2
	wg.Add(1)
	go func() {
		fmt.Println("Goroutine 2 quiere adquirir recurso B")
		B.Lock()
		fmt.Println("Goroutine 2 adquirió recurso B")
		fmt.Println("Goroutine 2 quiere adquirir recurso A")
		// Simular un retraso de 1 segundo
		time.Sleep(1 * time.Second)
		A.Lock()
		fmt.Println("Goroutine 2 adquirió recurso A")
		A.Unlock()
		B.Unlock()
		wg.Done()
	}()
	//Agregar temporizador
	timer := time.NewTimer(2 * time.Second)
	<-timer.C

	// Liberar goroutines
	wg.Wait()
	fmt.Println("Ambas goroutines terminaron")
}
