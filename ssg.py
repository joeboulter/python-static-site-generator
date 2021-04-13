import typer
import Site from ssg.Site

def main(source = "content", dest = "dist"):
    config = {'source' = source, 'dest' = dest}
    site = Site(**config).build()

typer.run(main())
