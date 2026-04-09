# Known Issues / Deuda Técnica

Issues conocidos del proyecto base (nachoyegro) que conviene resolver antes de ir a producción.

---

## Crítico

### Profile no se crea automáticamente al crear un User

**Síntoma:** `RelatedObjectDoesNotExist: User has no profile` al entrar al admin.

**Causa:** El modelo `Profile` tiene una relación OneToOne con `User`, pero no hay signal ni lógica que lo cree automáticamente cuando se crea un superuser (ni via `createsuperuser` ni via admin).

**Fix temporal:** Correr manualmente después de `createsuperuser`:

```bash
docker-compose exec backend python3 alumnos/manage.py shell -c "from django.contrib.auth.models import User; from core.models import Profile; admin = User.objects.get(username='admin'); Profile.objects.get_or_create(user=admin); print('Profile creado para:', admin.username)"
```

**Fix correcto:** Agregar un `post_save` signal en `core/models.py` que cree el Profile automáticamente al crear cualquier User:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

---

## Menor

### Warning: `version` obsoleto en docker-compose.yml

**Síntoma:** `the attribute 'version' is obsolete, it will be ignored` al correr cualquier comando de docker-compose.

**Causa:** Docker Compose v2 deprecó el campo `version` en el archivo.

**Fix:** Eliminar la línea `version: '3.8'` del `docker-compose.yml`.

---

### El usuario admin necesita carreras asignadas en su Profile

Después de crear el Profile, hay que asignarle las carreras desde el admin para que el sistema filtre correctamente los datos que puede ver: <http://localhost:8800/admin/core/profile/>
