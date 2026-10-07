# 05. Configuración de Redes Inalámbricas (WLAN) y Controlador Empresarial (WLC)

## Especificaciones Técnicas
* **Entorno de Simulación:** Cisco Packet Tracer (v8.0+)
* **Dispositivos Inalámbricos:** Wireless LAN Controller (WLC 3504), Home Wireless Router, Access Points (LAP/FlexConnect)
* **Protocolos de Red y Seguridad:** WPA2-Personal (PSK), WPA2-Enterprise (802.1X / EAP), IEEE 802.11a/b/g/n, DHCP, DNS, SNMP
* **Servicios de Red y Autenticación:** Servidor RADIUS (AAA), Servidor Web (HTTP), Servidor SNMP
* **Arquitectura de Red:** Segmentación por VLANs (VLAN 2, VLAN 5), Subinterfaces de Capa 2/3, Modo FlexConnect (*Local Switching* & *Local Authentication*)
* **Estructura:** Archivo de topología de Cisco Packet Tracer (`.pkt`)

---

## Descripción del Proyecto
Este proyecto aborda la planificación, despliegue y validación de redes inalámbricas (WLAN) abarcando desde entornos residenciales/SOHO hasta arquitecturas empresariales escalables y centralizadas mediante un controlador inalámbrico (WLC).

El desarrollo abarca los siguientes componentes clave:

1. **Red Inalámbrica Residencial (SOHO):**
   * **Configuración LAN/WAN y DHCP:** Implementación de un router doméstico con subred `/27` (`192.168.6.1/27`), servidor DHCP limitado a 20 usuarios y asignación de servidor DNS estático.
   * **Seguridad y Asociación:** Configuración del SSID `HomeSSID` en banda de 2.4 GHz con cifrado WPA2-Personal (AES) y asociación dinámica de clientes (Laptop, Tablet PC, Smartphone).

2. **Infraestructura Empresarial Centralizada (WLC):**
   * **Gestión y Subinterfaces Virtuales:** Configuración del WLC (`192.168.100.254`) a través de interfaz gráfica HTTPS, creando subinterfaces para segmentar el tráfico por VLAN (VLAN 2 para WPA2-PSK y VLAN 5 para WPA2-Enterprise).
   * **Autenticación 802.1X y RADIUS:** Integración de la red empresarial (`SSID-5`) con un servidor RADIUS externo (`10.6.0.254`) para la validación de usuarios individuales.
   * **Optimización con FlexConnect:** Habilitación de conmutación y autenticación local en los puntos de acceso para asegurar el procesamiento eficiente del tráfico de datos.

---

## Imágenes

**Topología inalámbrica simulada en Cisco Packet Tracer**
<img src="images/01-topologia.png" width="720" alt="Topología en Packet Tracer" />

**Verificación de conectividad (ping) desde un cliente inalámbrico**
<img src="images/02-ping-cliente.png" width="720" alt="Ping desde cliente inalámbrico" />

**Direccionamiento IP obtenido por DHCP (`ipconfig`)**
<img src="images/03-ipconfig.png" width="720" alt="Direccionamiento IP por DHCP" />

---

## Instrucciones de Ejecución

1. Abrir la topología de red **`Practica5-6_WLAN.pkt`** en **Cisco Packet Tracer** (versión 8.0 o superior).
2. Desde la PC **Administrador de empresa**, abrir el navegador web e ingresar a `https://192.168.100.254` (Usuario: `admin` / Contraseña: `Cisco123`) para verificar las WLANs, subinterfaces y parámetros SNMP/RADIUS.
3. Comprobar que los clientes inalámbricos residenciales (Laptop, Tablet, Smartphone) hayan obtenido direccionamiento IP automático en la subred `192.168.6.0/27`.
4. Verificar la autenticación en **Wireless Host 2** conectándose a `SSID-5` mediante 802.1X con el usuario `userWLAN5` y contraseña `userW5pass`.
5. Ejecutar un `ping` y abrir el navegador web hacia la dirección IP del **Servidor Web** (`203.0.113.78`) desde cualquier cliente para confirmar conectividad end-to-end.

---
