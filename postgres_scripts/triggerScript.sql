CREATE OR REPLACE FUNCTION updatePermissions() RETURNS trigger AS $$
DECLARE
  temprole RECORD;
  tempdb RECORD;
  roleid INT;
BEGIN
  IF (NEW.permission_id=60) THEN
    FOR temprole IN
      select pvr.* from dbs d, tables tb, ab_view_menu vm, ab_permission_view_role pvr, ab_permission_view pv
      where 
      tb.perm = (select name from ab_view_menu where id=NEW.view_menu_id) and
      d.id= tb.database_id and
      vm.name = d.perm and
      vm.id = pv.view_menu_id and
      pv.id = pvr.permission_view_id and
      pv.permission_id=60
      LOOP
        insert into ab_permission_view_role (id, role_id, permission_view_id) VALUES ( nextval('ab_permission_view_role_id_seq'), temprole.role_id, NEW.id );
      END LOOP;
    FOR tempdb IN
      select d.* from ab_view_menu vm, dbs d 
        where NEW.view_menu_id = vm.id and vm.name = d.perm
        LOOP
          roleid := nextval('ab_role_id_seq');
          insert into ab_role (id, name) VALUES ( roleid, 'datarole-'||tempdb.database_name );
          insert into ab_permission_view_role (id, role_id, permission_view_id) VALUES ( nextval('ab_permission_view_role_id_seq'), roleid, NEW.id );
        END LOOP;
  END IF;
  RETURN NULL;
END;

$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS updatePermissions on ab_permission_view;

CREATE TRIGGER updatePermissions AFTER INSERT ON ab_permission_view
  FOR EACH ROW EXECUTE PROCEDURE updatePermissions();
