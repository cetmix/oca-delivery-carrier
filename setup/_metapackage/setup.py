import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-delivery-carrier",
    description="Meta package for oca-delivery-carrier Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_delivery_carrier_files',
        'odoo14-addon-base_delivery_carrier_label',
        'odoo14-addon-carrier_account_environment',
        'odoo14-addon-delivery_auto_refresh',
        'odoo14-addon-delivery_carrier_agency',
        'odoo14-addon-delivery_carrier_category',
        'odoo14-addon-delivery_carrier_city',
        'odoo14-addon-delivery_carrier_customer_info',
        'odoo14-addon-delivery_carrier_default_tracking_url',
        'odoo14-addon-delivery_carrier_deposit',
        'odoo14-addon-delivery_carrier_info',
        'odoo14-addon-delivery_carrier_label_batch',
        'odoo14-addon-delivery_carrier_location',
        'odoo14-addon-delivery_carrier_multi_zip',
        'odoo14-addon-delivery_carrier_package_measure_required',
        'odoo14-addon-delivery_carrier_partner',
        'odoo14-addon-delivery_carrier_pricelist',
        'odoo14-addon-delivery_carrier_return_barcode_pattern',
        'odoo14-addon-delivery_correos_express',
        'odoo14-addon-delivery_cttexpress',
        'odoo14-addon-delivery_free_fee_removal',
        'odoo14-addon-delivery_multi_destination',
        'odoo14-addon-delivery_package_fee',
        'odoo14-addon-delivery_package_number',
        'odoo14-addon-delivery_packaging_archive',
        'odoo14-addon-delivery_postlogistics',
        'odoo14-addon-delivery_postlogistics_dangerous_goods',
        'odoo14-addon-delivery_postlogistics_server_env',
        'odoo14-addon-delivery_price_collection_cost',
        'odoo14-addon-delivery_price_collection_cost_product_domain',
        'odoo14-addon-delivery_price_method',
        'odoo14-addon-delivery_price_product_domain',
        'odoo14-addon-delivery_price_rule_untaxed',
        'odoo14-addon-delivery_purchase',
        'odoo14-addon-delivery_roulier',
        'odoo14-addon-delivery_roulier_chronopost_fr',
        'odoo14-addon-delivery_roulier_laposte_fr',
        'odoo14-addon-delivery_roulier_option',
        'odoo14-addon-delivery_schenker',
        'odoo14-addon-delivery_schenker_picking_volume',
        'odoo14-addon-delivery_schenker_quant_package_dimension',
        'odoo14-addon-delivery_send_to_shipper_at_operation',
        'odoo14-addon-delivery_state',
        'odoo14-addon-delivery_tnt_oca',
        'odoo14-addon-delivery_ups_oca',
        'odoo14-addon-partner_default_delivery_carrier',
        'odoo14-addon-partner_delivery_zone',
        'odoo14-addon-server_environment_delivery',
        'odoo14-addon-stock_picking_carrier_from_rule',
        'odoo14-addon-stock_picking_delivery_link',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
