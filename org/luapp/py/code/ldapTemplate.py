# -*- coding:UTF-8 -*-

'''
Created on 2014-12-10

@author: gaohongtao
'''
import random
from string import Template

gTxt = open('C:\\Users\\nq\\Desktop\\template_group.ldif', 'wb')
uTxt = open('C:\\Users\\nq\\Desktop\\template_user.ldif', 'wb')

groupTpl = '''dn: ${dn}
objectClass: top
objectClass: organizationalUnit
ou: ${ou}

'''

userTpl = '''dn: uid=user_${ff}_${u1},${dn}
objectClass: posixAccount
objectClass: top
objectClass: inetOrgPerson
gidNumber: 0
givenName: first_${ff}_${u1}
sn: sec_${ff}_${u1}
displayName: dis_${ff}_${u1}
uid: user_${ff}_${u1}
homeDirectory: home_${ff}_${u1}
telephoneNumber: 1111${kk}${u1}
mail: aa_${ff}_${u1}@bb.com
cn: dis_${ff}_${u1}
uidNumber: ${kk}

'''

kk = 1

maxUser = 10

for i in range(1, 11):
    dn = 'ou=ou_%s,dc=maxcrc,dc=com' % i
    ou = 'ou_%s' % i
    t = Template(groupTpl)
    gTxt.write(t.substitute(dn=dn, ou=ou))

    for u1 in range(random.randint(0, maxUser)):
        kk += 1
        t = Template(userTpl)
        uTxt.write(t.substitute(dn=dn, u1=u1, ff=i, kk=kk))

    for j in range(1, 11):
        dn = 'ou=ou_%s_%s,ou=ou_%s,dc=maxcrc,dc=com' % (i, j, i)
        ou = 'ou_%s_%s' % (i, j)
        t = Template(groupTpl)
        gTxt.write(t.substitute(dn=dn, ou=ou))

        for u1 in range(random.randint(0, maxUser)):
            kk += 1
            t = Template(userTpl)
            uTxt.write(t.substitute(dn=dn, u1=u1, ff='%d_%d' % (i, j), kk=kk))

        for m in range(1, 11):
            dn = 'ou=ou_%s_%s_%s,ou=ou_%s_%s,ou=ou_%s,dc=maxcrc,dc=com' % (i, j, m, i, j, i)
            ou = 'ou_%s_%s_%s\n' % (i, j, m)
            t = Template(groupTpl)
            gTxt.write(t.substitute(dn=dn, ou=ou))

            for u1 in range(random.randint(0, maxUser)):
                kk += 1
                t = Template(userTpl)
                uTxt.write(t.substitute(dn=dn, u1=u1, ff='%d_%d_%d' % (i, j, m), kk=kk))

            for n in range(1, 11):
                dn = 'ou=ou_%s_%s_%s_%s,ou=ou_%s_%s_%s,ou=ou_%s_%s,ou=ou_%s,dc=maxcrc,dc=com' % (
                    i, j, m, n, i, j, m, i, j, i)
                ou = 'ou_%s_%s_%s_%s\n' % (i, j, m, n)
                t = Template(groupTpl)
                gTxt.write(t.substitute(dn=dn,ou=ou))

                for u1 in range(random.randint(0, maxUser)):
                    kk += 1
                    t = Template(userTpl)
                    uTxt.write(t.substitute(dn=dn, u1=u1, ff='%d_%d_%d_%d' % (i, j, m, n), kk=kk))

gTxt.close()
uTxt.close()