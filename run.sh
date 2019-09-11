read -p "input NodeNumber :" valnum echo $valnum
read -p "input DB password :" val echo $val
yum install git vim htop wget -y
cd /root
yum -y install python-setuptools
easy_install pip
git clone https://github.com/StartZYP/shadowsocks.git
cd /root/shadowsocks
pip install -r requirements.txt
cp apiconfig.py userapiconfig.py
cp config.json user-config.json
sed -ig 's/{NODE}/'$valnum'/g' /root/shadowsocks/userapiconfig.py
sed -ig 's/{HOST}/www.ipedg.com/g' /root/shadowsocks/userapiconfig.py
sed -ig 's/{PORT}/23306/g' /root/shadowsocks/userapiconfig.py
sed -ig 's/{USER}/root/g' /root/shadowsocks/userapiconfig.py
sed -ig 's/{PASS}/'$val'/g' /root/shadowsocks/userapiconfig.py
sed -ig 's/{DB}/ssrpanel/g' /root/shadowsocks/userapiconfig.py
chmod +x /root/shadowsocks/run.sh