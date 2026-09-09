import json
import os
from datetime import datetime
from typing import Dict, List

class PermissionManager:
    def __init__(self, permissions_file="permissions.json"):
        self.permissions_file = permissions_file
        self.permissions = self._load_permissions()
        self.audit_log = []

    def _load_permissions(self) -> Dict:
        """Charger les permissions depuis le fichier"""
        if os.path.exists(self.permissions_file):
            with open(self.permissions_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_permissions(self):
        """Sauvegarder les permissions"""
        with open(self.permissions_file, 'w') as f:
            json.dump(self.permissions, f, indent=2)

    def request_permission(self, permission: str, reason: str = "") -> bool:
        """Demander une permission à l'utilisateur"""
        if permission in self.permissions:
            return self.permissions[permission]

        print(f"\n{'='*60}")
        print(f"🔐 DEMANDE DE PERMISSION")
        print(f"{'='*60}")
        print(f"Permission: {permission}")
        if reason:
            print(f"Raison: {reason}")
        print(f"\nVoulez-vous autoriser cette action? (oui/non): ", end="")
        
        response = input().strip().lower()
        authorized = response in ['oui', 'yes', 'o', 'y']
        
        self.permissions[permission] = authorized
        self._save_permissions()
        
        self._log_permission_request(permission, authorized, reason)
        return authorized

    def _log_permission_request(self, permission: str, authorized: bool, reason: str):
        """Logger les demandes de permission"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'permission': permission,
            'authorized': authorized,
            'reason': reason
        }
        self.audit_log.append(log_entry)
        with open('permission_audit.log', 'a') as f:
            f.write(f"{log_entry}\n")

    def has_permission(self, permission: str) -> bool:
        """Vérifier si une permission est accordée"""
        return self.permissions.get(permission, False)

    def revoke_permission(self, permission: str):
        """Révoquer une permission"""
        self.permissions[permission] = False
        self._save_permissions()

    def grant_permission(self, permission: str):
        """Accorder une permission"""
        self.permissions[permission] = True
        self._save_permissions()

    def list_permissions(self) -> Dict:
        """Lister toutes les permissions"""
        return self.permissions.copy()

    def reset_permissions(self):
        """Réinitialiser toutes les permissions"""
        self.permissions = {}
        self._save_permissions()
