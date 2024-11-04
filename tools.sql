
SELECT C.dni "DNI", CONCAT(apellido, ", ", nombre) "Apellido y Nombre", sueldo 
FROM contratos C inner join personas P ON C.dni=P.dni
WHERE nro_contrato=5;

ifnull(fecha_caducidad, "Sin Fecha");

LOWER(razon_social);

DATE_FORMAT(fecha_incorporacion, "%d/%m/%Y") "Fecha inicio";

DATE_FORMAT(ADDDATE(date(now()), INTERVAL 2 MONTH), "%d/%m/%Y") "fecha de vencimiento"

select ADDDATE(date(now()), INTERVAL 2 MONTH);

date_add(fecha_solicitud, INTERVAL 30 DAY)

datediff(fecha_finalizacion_contrato, fecha_caducidad)

CONCAT(nombre, " ", apellido) "Nombre y apellido", DATE_FORMAT(fecha_nacimiento, "%d/%m/%Y") "fecha_nacimiento",
DAY(fecha_nacimiento) "Día", MONTH(fecha_nacimiento) "Mes", YEAR(fecha_nacimiento) "Año"

concat("$", SUM(importe_comision))

STD(resultado) "Desvío STD", VARIANCE(resultado)

 ROUND(count(fecha_pago) / COUNT(*) * 100, 2) "% comisiones pagas", 
 
 MAX(sueldo)
 
 ROUND(AVG(COM.importe_comision), 2)
 
 select * from personas where apellido like 'G%';
 
 sum(com.importe_comision)
 
 
 count(fecha_pago)/count(com.nro_contrato)*100, (count(com.nro_contrato)-count(fecha_pago))/count(com.nro_contrato)*100 -- Para calcular promedios
 
 
 drop TEMPORARY TABLE if EXISTS fechas ;
create TEMPORARY TABLE fechas (select nom_plan, max(fecha_desde_plan) as fecha from valores_plan GROUP BY nom_plan);

 set @ult_id=last_insert_id();
select @ult_id;